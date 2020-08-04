"use strict"

const $cupcakesList = $("#cupcakes-list")
const $addCupcakeForm = $("#add-cupcake-form")

// Gets the list of cupcakes from the API and returns
// can use map here!!!
async function getCupcakes() {
    let cupcakes = [];
    let response = await axios.get("/api/cupcakes");
    for (let cupcake of response.data.cupcakes) {
        const {flavor, size, rating, image} = cupcake;
        cupcakes.push({flavor, size, rating, image});
    }
    return cupcakes;
}

// this function is doing more than just populating - also gettin gthe list - could update the name - or break apart
async function populateCupcakesList() {
    // let cupcakes = await getCupcakes();
    $cupcakesList.empty();
    for (let cupcake of cupcakes) {
        let $newLi = $("<li>")
        let $liMarkup = $(`
            <p>Flavor: ${cupcake.flavor}</p>
            <p>Size: ${cupcake.size}</p>
            <p>Rating: ${cupcake.rating}</p>
            <img src=${cupcake.image} alt=${cupcake.flavor}>
        `)
        $newLi.append($liMarkup)
        $cupcakesList.append($newLi)
    }
}

// don't need the $ because these arn't JQ objects - also helps the object we create at the bottom
async function handleSubmit(e){
    e.preventDefault();
    
    let $flavor = $('#flavor').val()
    let $size = $('#size').val()
    let $rating = $('#rating').val()
    let $image_url = $('#image_url').val()
    
    await axios.post('/api/cupcakes', {flavor: $flavor, size: $size, rating: $rating, image: $image_url})
    
    let cupcakes = await getCupcakes();

    await populateCupcakesList(cupcakes);
}

$addCupcakeForm.on('submit', handleSubmit)

$(async function() {
    await populateCupcakesList();
});