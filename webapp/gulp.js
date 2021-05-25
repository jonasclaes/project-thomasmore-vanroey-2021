const gulp = require('gulp');

// Needed for development (gulp)
const browserSync = require('browser-sync').create();
const plumber = require('gulp-plumber');
const notify = require('gulp-notify');
const newer = require('gulp-newer');
const sass = require('gulp-dart-sass');
const prefix = require('gulp-autoprefixer');
const sourcemaps = require('gulp-sourcemaps');
const postcss = require('gulp-postcss');
const mqpacker = require('@lipemat/css-mqpacker');

// Needed for production (gulp build)
const del = require('del');
const fs = require('fs');
const realFavicon = require('gulp-real-favicon');
const imagemin = require('gulp-imagemin');
const minify = require('gulp-minifier');





// Live-reload the browser
gulp.task('browser-sync', () => {
    browserSync.init({
        startPath: '/index.html',
        port: 7777,
        server: {
            baseDir: './src',
            directory: true,
        },
        ui: {
            port: 7779,
        },
    });
    // gulp.watch('./scss/**/*.scss', gulp.series('sass'));
    gulp.watch('./src/**/*.{html,css,js}').on('change', browserSync.reload);
});

// Delete all files and folders inside the dist folder
gulp.task('clean', () => del(['dist/**/*']));

// Copy files from ./src to ./dist
gulp.task('copy', () => gulp.src('./src/**/*').pipe(gulp.dest('./dist')));

// RealFavIcon config
const FAVICON = {
    name: 'My App', // The name for your mobile app
    startImage: './favicon.png', // Original image (min 512*521 px) to start from
    destination: './dist/assets/icons', // Save generated icons and config files inside this folder
    androidThemeColor: '#ffffff', // Theme color for Android app
    dataFile: './dist/assets/icons/faviconData.json',
};

// Generatie real favicon
// https://realfavicongenerator.net/api/non_interactive_api#.YBPxQej0m0o
gulp.task('generate-favicon', (cb) => {
    realFavicon.generateFavicon(
        {
            masterPicture: FAVICON.startImage,
            dest: FAVICON.destination,
            iconsPath: '/assets/icons',
            design: {
                ios: {
                    pictureAspect: 'noChange',
                    assets: {
                        ios6AndPriorIcons: false,
                        ios7AndLaterIcons: false,
                        precomposedIcons: false,
                        declareOnlyDefaultIcon: true,
                    },
                },
                desktopBrowser: {
                    design: 'raw',
                },
                windows: {
                    pictureAspect: 'noChange',
                    backgroundColor: '#da532c',
                    onConflict: 'override',
                    assets: {
                        windows80Ie10Tile: false,
                        windows10Ie11EdgeTiles: {
                            small: false,
                            medium: true,
                            big: false,
                            rectangle: false,
                        },
                    },
                },
                androidChrome: {
                    pictureAspect: 'shadow',
                    themeColor: FAVICON.androidThemeColor,
                    manifest: {
                        name: FAVICON.name,
                        startUrl: '/',
                        display: 'standalone',
                        orientation: 'notSet',
                        onConflict: 'override',
                        declared: true,
                    },
                    assets: {
                        legacyIcon: false,
                        lowResolutionIcons: true,
                    },
                },
                safariPinnedTab: {
                    pictureAspect: 'silhouette',
                    themeColor: '#5bbad5',
                },
            },
            settings: {
                scalingAlgorithm: 'Mitchell',
                errorOnImageTooSmall: true,
                readmeFile: false,
                htmlCodeFile: true,
                usePathAsIs: false,
            },
            markupFile: FAVICON.dataFile,
        },
        () => {
            cb();
        }
    );
});

// Inject the favicon markup in all your HTML pages
gulp.task('inject-favicon-markup', () =>
    gulp
        .src(['./dist/**/*.html'])
        .pipe(realFavicon.injectFaviconMarkups(JSON.parse(fs.readFileSync(FAVICON.dataFile)).favicon.html_code))
        .pipe(gulp.dest('./dist'))
);

// Minify all files in dist folder
gulp.task('minify', () =>
    gulp
        .src('./dist/**/*')
        .pipe(
            imagemin([
                imagemin.gifsicle({ interlaced: true }),
                imagemin.mozjpeg({ quality: 70, progressive: true }),
                imagemin.optipng({ optimizationLevel: 5, interlaced: true }),
                imagemin.svgo({
                    plugins: [{ removeViewBox: true }, { cleanupIDs: false }],
                }),
            ])
        )
        .pipe(
            minify({
                minify: true,
                minifyHTML: {
                    collapseWhitespace: true,
                    conservativeCollapse: true,
                    removeComments: true,

                    minifyCSS: true, // minify inline CSS
                },

                minifyCSS: true,
            })
        )
        .pipe(gulp.dest('./dist'))
);

// gulp.task('build', gulp.series('clean','copy', 'generate-favicon', 'inject-favicon-markup', 'minify'));
gulp.task('build', gulp.series('clean','copy', 'minify'));
gulp.task('default', gulp.series( 'browser-sync'));
