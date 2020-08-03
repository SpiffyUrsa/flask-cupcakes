"use strict"

const $cupcakesList = $("#cupcakes-list")
const $addCupcakeForm = $("#add-cupcake-form")

// Gets the list of cupcakes from the API and returns 
async function getCupcakes() {
    let cupcakes = [];
    let response = await axios.get("/api/cupcakes");
    for (let cupcake of response.data.cupcakes) {
        const {flavor, size, rating, image} = cupcake;
        cupcakes.push({flavor, size, rating, image});
    }
    return cupcakes;
}

async function populateCupcakesList() {
    let cupcakes = await getCupcakes();
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

$(function() {
    populateCupcakesList();
});