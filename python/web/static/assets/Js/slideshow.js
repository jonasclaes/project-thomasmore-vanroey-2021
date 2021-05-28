let indexNum =
    0;
const time = 5000; //the time between the different captions/pictures

//create an array including all images
const images = [
    '2019_Ruckus-EMEA-Cloud-Partner-Of-the-Year-Hans-en-Roel-Munchen-LifeatVanRoey.jpg',
    'Digital-Experience-Center-bar-lifeatvanroey.jpg',
    'Yves-presentatie-Dynamics-365-Lifeatvanroey.jpg',
    'Nicolas-doet-Hololens-aan-Lifeatvanroey.jpg',
    'sneakpeek-studenten-next-gen-lifeatvanroey.jpg',
    'VanRoey.be-nieuwbouw-render.jpg',
    'VanRoeybe-Charity-Quiz-Overhandiging-cheques.jpg',
    'Vision-Event-2019-Sfeerbeeld-LifeatVanRoey.jpg',
    'Yves-presentatie-Dynamics-365-Lifeatvanroey.jpg'
]

function imageToggler() {
    // go to the next step
    indexNum = indexNum + 1 < images.length ? (indexNum += 1) : 0;
    //wait before actually showing the next step
    setTimeout(imageToggler, time);
    //show the next step
    document.querySelector('body').style.backgroundImage = `url('/static/assets/images/${images[indexNum]}')`
}

imageToggler()

