# Phase III: Prototypes and User Testing

## Introduction

MyPantry is a web app currently in development with the goal of helping users find recipes based on ingredients they already have at home. In this third report, we the UX team (Todd Lange, Ethan Nguyen, and Dylan Wright) will provide insight into our findings regarding the usability of early prototypes for MyPantry.

## Methods

With our main prototype built out using the web framework Django, we ran a usability user test (n = 5). To guide participants to use each feature in our prototype, each participant was given the following four tasks:

1. You have these ingredients in your kitchen (hand participant list of ingredients). Walk me through how you would go about finding a meal you can cook using only these ingredients.
2. Let’s say you want to plan out everything you’ll be cooking this week. How would you go about doing that task? 
   * Now you’re getting ready to go shopping, and you want to figure out what you’ll need to buy at the store. How do you think you would figure that out?
3. Now let’s move on and say that you absolutely love your Grandma’s potato salad recipe (hand user recipe card). How would you go about adding this recipe to your planner?
4. Now you recently had stomach problems after having eaten too much of your potato salad. How would you go about logging your experience so you can share it later with your doctor?

For each task, we kept note of if users were successful in accomplishing the task, how users accomplished the task, and asked questions following the task to gain insight into how they thought it went. We also collected background information to see if MyPantry was a software that users would have a need for.

## Findings

### Background information

* 3 / 5 participants reported rarely to never cooking their own meals.
* When asked how participants decided what they wanted to cook (excluding participants who never cooked) all participants mentioned that it is mostly driven by feelings of what they currently desire; no participants use a cookbook.
* 4 / 5 participants reported sharing grocery shopping responsibilities and occasionally going grocery shopping themselves. One participant reported being solely responsible.
* 60% of participants used a note-taking app or physical list to keep track of items needed for grocery shopping with the remaining 40% relying solely on memory.

### Task 1: Finding Recipe Based on Ingredients

* 80% of participants successfully accomplished the task and used the pantry tab to enter in all their ingredients and use the “Filter Recipes” filter on the Browse Recipes page. The participant who was not able to accomplish the task found the filter but did not select the ingredients from the “Pantry” tab.
* 80% of participants did not immediately identify the “Pantry” and “Browse Recipes” tabs as the two tabs required for this task.
  * One participant reported the tab names being confusing and not being sure what “Pantry” was referring to; 20% of participants did not go to the “Pantry” tab first.
* The average participant ranking for the difficulty of the task (on a scale of 1-5 where 1 is easy and 5 is difficult) was 2.8, with 1 participant giving the task a 2 and all others giving it a 3.

### Task 2: Add Recipe to Grocery List and Finding Missing Ingredients

* 80% of participants successfully found and imported the desired recipe into the grocery list and recognized missing ingredients within the “Grocery List” tab
  * One participant did not identify the “Import to Grocery List” button and opted to manually identify missing ingredients.
  * Another participant initially had issues with identifying that same button and instead selected the save recipe button (heart icon), but later identified the “Import to Grocery List” button.
* All users reported ease of this task with the average rating across both tasks (the first task of planning a recipe and the second task of identifying missing ingredients) being 1.1 (on a scale of 1-5).

### Task 3: Importing Custom Recipe to MyPantry

* All participants were able to identify and correctly enter a custom recipe into MyPantry.
* 3 / 5 participants were confused about the meaning of “Genre” in the custom recipe form.
  * One participant mentioned a desire to create custom genres.
* One participant mentioned the desire to have recipes be imported by URL
* 40% of participants noted that the “Add Step” icon was too small.
* The average difficulty rating was 1.8 with four participants rating it a 2 and one participant rating it a 1.

### Task 4: Add Entry to Food Diary

* All participants were able to successfully reach and submit the food diary form entry form.
* 60% of participants, however, did not use the “Import to Food Diary” button and instead selected the “Add Manual Entry” button (a feature meant for recipes that are not already in MyPantry).
  * One of the participants that managed to successfully use the “Import to Food Diary” button mentioned that “it wasn't the way I wanted it to work”, expecting that the button would redirect users to the “Food Diary” tab.
* The average difficulty rating was 1.4 with 4 participants rating it a 1 and one participant rating it a 3.
* One participant mentioned that they would like the ability to edit food diary entries after they have been submitted.
* Two participants mentioned that they were unlikely to get much use out of the Food Diary in its current form, with one participant also saying that a timeline of what they have eaten and notes describing how they felt at a particular time would be much more valuable for them.

### Debrief Questions

* When asked what they liked about the prototype, 60% of participants mentioned the “Grocery List” tab with one participant saying “I liked how automatic it was”.
* When asked what participants disliked about the prototype, various things were mentioned including: confusing titles for tabs, adding items to the food diary, unclear what favoriting a recipe does, and adding ingredients in the “Pantry” tab was a lot of work.
* Additional features recommended by participants included:
  * feature to check off items on the grocery list
  * in the recipe card view, the ability to favorite and import the recipe
  * a way for the grocery list to be imported to note-taking apps

## Conclusions

Based on our findings we conclude that the design of MyPantry needs some more work to improve user experience and address concerns discovered during user testing.

We believe some of the issues discovered can be solved with minor changes, such as:
* In the “browse recipes” tab, filters can be reworded to provide more clarity into what their purposes are.
* Add buttons on the “Create Custom Recipe” form could be made a little larger.
* The submit button for the “Create Custom Recipe” form could be made dynamically to fit to how many steps the user added in their recipe (instead of always being fixed at the bottom of the page).
* The home page “help and getting started” documentation can be laid out more clearly. Most users did not click through the carousel of documentation and ignored it completely.

The food diary tab, however, will likely need to be reworked entirely. User testing indicated that many participants had difficulty with how we laid out features for the Food Diary. We believe that a suggestion given by one of the participants is the best way to move forward for this feature; instead of having a Food Diary and a separate Reaction Reporter, incorporating it all into a timeline where users can say what recipes they have eaten and how they currently feel may be more useful to users. 

## Caveats

While we have gained valuable insight from our user testing, there are still important caveats to note. All participants of our user testing are in some capacity involved with the Usability course. This is not likely to be representative of the average user that MyPantry hopes to target and as such, there may be additional flaws with our prototype that would affect the average users and that did not surface during user testing.

