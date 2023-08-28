// Get all the select-menu elements
const optionMenus = document.querySelectorAll(".select-menu");

// Iterate through each select-menu
optionMenus.forEach(optionMenu => {
  const selectBtn = optionMenu.querySelector(".select-btn");
  const options = optionMenu.querySelectorAll(".option");
  const sBtn_text = optionMenu.querySelector(".sBtn-text");

  selectBtn.addEventListener("click", () => optionMenu.classList.toggle("active"));

  options.forEach(option => {
    option.addEventListener("click", () => {
      let selectedOption = option.querySelector(".option-text").innerText;
      sBtn_text.innerText = selectedOption;
      optionMenu.classList.remove("active");
    });
  });
});
const wrapper = document.querySelector(".wrapper"),
selectBtn = wrapper.querySelector(".select-btn"),
searchInp = wrapper.querySelector("input"),
options = wrapper.querySelector(".options");

//array of some countries//
let countries = ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh",
                "Bhutan", "Brunei", "Cambodia", "China", "Cyprus", "East Timor",
                "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan",
                "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon",
                "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea",
                "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Saudi Arabia",
                "Singapore", "South Korea", "Sri Lanka", "Syria", "Taiwan", "Tajikistan",
                "Thailand", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan",
                "Vietnam", "Yemen"];

function addCountry(){
    options.innerHTML ="";
    countries.forEach(country => {
        // adding each country inside li
        let li = `<li onclick="updateName(this)">${country}</li>`;
        options.insertAdjacentHTML("beforeend", li);
    });
}
function updateName(selectedLi){
    searchInp.value = "";
    addCountry();
    wrapper.classList.remove("active");
    selectBtn.firstElementChild.innerText = selectedLi.innerText;
}

searchInp.addEventListener("keyup", () => {
    let arr = [];
    let searchedVal = searchInp.value.toLowerCase();
    arr = countries.filter(data => {
        return data.toLowerCase().startsWith(searchedVal);
    }).map(data => `<li onclick="updateName(this)">${data}</li>`).join("");
    options.innerHTML = arr ? arr : `<p>Oops! Country not found here</p>`;
});

addCountry();
selectBtn.addEventListener("click", ()=> {
    wrapper.classList.toggle("active");
});
const wrapper1 = document.querySelector(".wrapper1"),
selectBtn1 = wrapper1.querySelector(".select-btn1"),
searchInp1 = wrapper1.querySelector("input"),
options1 = wrapper1.querySelector(".options1");
let cities = [  "Agra", "Ahmedabad", "Allahabad", "Amritsar",
"Bengaluru", "Bhopal", "Bhubaneswar",
"Chandigarh", "Chennai", "Coimbatore", "Cuttack",
"Delhi",
"Goa", "Gorakhpur", "Gurgaon", "Guwahati",
"Hyderabad",
"Indore",
"Jaipur", "Jammu", "Jamshedpur", "Jodhpur",
"Kanpur", "Kochi", "Kolkata", "Kota",
"Lucknow", "Ludhiana",
"Madurai", "Mangalore", "Mumbai", "Mysore",
"Nagpur", "Noida",
"Patna","Puri", "Pune","Pondicherry","Patiala",
"Raipur", "Rajkot", "Ranchi",
"Srinagar", "Surat","Shiliguri","Shillong","Shimla",
"Thane", "Thiruvananthapuram","Tezpur",
"Vadodara", "Varanasi", "Vijayawada", 
];
function addCity(){
    options1.innerHTML ="";
    cities.forEach(City => {
        // adding each city inside li
        let li = `<li onclick="updateName1(this)">${City}</li>`;
        options1.insertAdjacentHTML("beforeend", li);
    });
}
function updateName1(selectedLi){
    searchInp1.value = "";
    addCountry();
    wrapper1.classList.remove("active");
    selectBtn1.firstElementChild.innerText = selectedLi.innerText;
}
searchInp1.addEventListener("keyup", () => {
    let arr = [];
    let searchedVal1 = searchInp1.value.toLowerCase();
    arr = cities.filter(data => {
        return data.toLowerCase().startsWith(searchedVal1);
    }).map(data => `<li onclick="updateName1(this)">${data}</li>`).join("");
    options1.innerHTML = arr ? arr : `<p>Oops! City not found here</p>`;
});
addCity();
selectBtn1.addEventListener("click", ()=> {
    wrapper1.classList.toggle("active");
});