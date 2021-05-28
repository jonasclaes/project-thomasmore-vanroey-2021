//Define Arrays variables to store quotes
const mnumber = new Array(12);
const mcontent = new Array(12);

//Defining Quote. Why not from file? Might come with wrong ID
mnumber[0] = '1993: Groeibedrijf';
mcontent[0] = ' Van Roey Automation begon vanuit de Wieltjeshoeve op de Steenweg op Merksplas.\n' +
    '            Enorme groei legitimeerde een verhuis naar de huidige vestiging van de hoofdzetel in Kempenlaan 2\n' +
    '            in Turnhout. Later volgden vestigingen in Geel en Mechelen onder de naam VanRoey.be.';




//to choose milestone content AND paste it into HTML file
function Milestone12(){
    const lgdt = document.getElementById('milestoneBody'); //Getting element by #ID
    // Write out the quote as HTML
    lgdt.innerHTML = `<h1>${mnumber[0]}</h1><p class="float-right">${mcontent[0]}</p>`; //Pasting DIV into HTML with styling and new quote
    //lgbody.append(lgdt);
}

var element = document.getElementById("LinkID1");
element.onclick = function() {
    Milestone12();
}