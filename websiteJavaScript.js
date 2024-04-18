var url = "file:///Users/speedyburgers/GitHib/Group6-SP24/website_good.html";



function submit() {
    var calorieData = document.getElementById("calories").value;
    var carbData = document.getElementById("carbs").value;
    var fatData = document.getElementById("fats").value;
    var proteinData = document.getElementById("protein").value;
    var timeData = document.getElementById("date").value;
    var hallData = document.getElementById("dine").value;
    var retailData = document.getElementById("retail").value;
    var typeData = document.querySelector('#meal').value;

    console.log(timeData)
    console.log(typeData)
    console.log(hallData)
    console.log(retailData)
    console.log(calorieData)
    console.log(proteinData)
    console.log(carbData)
    console.log(fatData)

    postURL = url + "/getPlan";
    fetch (url, {
        method: "POST",
        body: JSON.stringify({
          calories: calorieData,
          protein: proteinData,
          carbs: carbData,
          fat: fatData,
          date: timeData,
          meal: typeData,
          hall: hallData,
          retail: retailData
          // fill in the rest of the paramters
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }}).then(data => {
          return data.json(); // the meal plan should be in data.json()
        });
      }