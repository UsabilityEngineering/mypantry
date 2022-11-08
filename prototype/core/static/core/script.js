// pantry

function checkboxClicked(box) {
    if(box.src.includes('/static/core/icons/check-square.svg')) {
        box.src = '/static/core/icons/square.svg';
        console.log('if');
    }
    else {
        box.src = '/static/core/icons/check-square.svg';
        console.log('else');
    }
}

// browse recipes

function saveRecipe(recipe) {
    if(recipe.src.includes('/static/core/icons/heart.svg')) {
        recipe.src = '/static/core/icons/heart-fill.svg';
    }
    else {
        recipe.src = '/static/core/icons/heart.svg';
    }
}

function addGrocList(recipe) {
    if(recipe.innerText == "Add Recipe Ingredients to Grocery List") {
        recipe.innerHTML = "Remove Recipe from Grocery List";
    }
    else {
        recipe.innerText = "Add Recipe Ingredients to Grocery List";
    }
}

function importRepFoodDiary(recipe) {
    if(recipe.innerText  == "Import Recipe to Food Diary") {
        recipe.innerText  = "Remove Recipe from Grocery List";
    }
    else {
        recipe.innerText  = "Import Recipe to Food Diary";
    }
}

function test() {
    console.log('hello there')
}





