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
        recipe.innerText = "Remove Recipe from Grocery List";
    }
    else {
        recipe.innerText = "Add Recipe Ingredients to Grocery List";
    }
}

function importRepFoodDiary(recipe) {
    if(recipe.innerText  == "Import Recipe to Food Diary") {
        recipe.innerText  = "Remove Recipe from Food Diary";
    }
    else {
        recipe.innerText  = "Import Recipe to Food Diary";
    }
}

function test() {
    console.log('hello there')
}

function fillRecipeName(recipe) {
    var recipe_name_span = document.getElementById('imported_recipe_name');
    var recipe_name_box = recipe_name_span.querySelector('input');
    
    var imported_recipe_name = recipe.parentElement.parentElement.querySelector('span')
    recipe_name_box.value = imported_recipe_name.innerText;
}





