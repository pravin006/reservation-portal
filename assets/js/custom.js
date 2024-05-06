function dt(){
    let dt = document.getElementById("teeTime").value;
    var value = document.getElementById("name_of").innerHTML;


    if (dt == ''){
        alert("Please select a date and time!");
    } else{
        $.ajax({
            url:"/selectdt",
        //   the second weight is from weight variable defined earlier
            type: "POST", 
            data:{dt: dt,
                name:value},
        //   dataType: 'json',   //you may use jsonp for cross origin request
        //   crossDomain: true,
            error: function() {
            alert("Error");
            },
            success: function(data, status, xhr){
                // add feedback
            }})
    }
}

if(document.getElementById("dt") != null){
    document.querySelector("#dt").addEventListener("click", dt);
}




function bmi(){

    // debugger
    /* Using Javascript & DOM Selectors */ 
    let height = document.getElementsByClassName("height_input")[0].value; /* https://www.w3schools.com/jsref/met_document_getelementsbyclassname.asp */
    /* let feet = document.querySelector(".feet").value; */

    /* Using Javascript & JQuery Selector */
    // let feet2 = $(".height_input")[0].value /* https://www.w3schools.com/jquery/jquery_ref_selectors.asp */

    var clearBtn = document.getElementById("clear");    // clearBtn is the DOM object
    var calcBtn = document.getElementById("bmi");


    // When I click on the calculate button, I want to set the userOn = 1
    // This will change the style of the clearBtn
    if (clearBtn.getAttribute("usrOn") == "0") {
        clearBtn.setAttribute("usrOn", "1")
        /* store away original background color and opacity */
        clearBtn.setAttribute("origC", getComputedStyle(clearBtn).backgroundColor);
        clearBtn.setAttribute("origO", getComputedStyle(clearBtn).opacity);
    } 

    /* flip to calcBtn background color and opacity */
    let color=calcBtn.getAttribute("origC");
    let opacity=getComputedStyle(calcBtn).opacity;

    // clearBtn.setAttribute("style", "background-color: " + color);
    // Not advisable to do the above: https://www.w3schools.com/jsref/met_element_setattribute.asp 
    clearBtn.style.backgroundColor=color;
    clearBtn.style.opacity=opacity;

    let weight = document.querySelector(".weight_input").value;


    // checked is a property of a radio button type
    // checked will be true (checked) or false (unchecked)
    if (document.getElementById('m').checked) {
        var aUnit = 'm'     

        // Front-End Calculation
        // var bmi = weight / Math.pow(height, 2)

    } else {
        var aUnit = 'cm'

        // var bmi = weight / Math.pow(height / 100, 2)
    }

    // debugger
    if (document.querySelector(".output_space > p").innerHTML=="The Output Area") {
        document.querySelector(".output_space > p").innerHTML=""
    }

    // if (bmi < 18.5) {
    //     document.querySelector("p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value is Under Weight"+"<br>";
    // } else if ((bmi >= 25) && (bmi <= 29.9)) {
    //     document.querySelector("p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value is Over Weight"+"<br>";
    // } else if (bmi >= 30) {
    //     document.querySelector("p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value is Obesse"+"<br>";
    // } else {
    //     document.querySelector("p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value normal"+"<br>";
    // }


    // if (bmi < 18.5) {
    //     document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value is Under Weight"+"<br>";
    // } else if ((bmi >= 25) && (bmi <= 29.9)) {
    //     document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value is Over Weight"+"<br>";
    // } else if (bmi >= 30) {
    //     document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value is Obesse"+"<br>";
    // } else {
    //     document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value normal"+"<br>";
    // }

    // call the /process route to calculate the bmi
    $.ajax({
      url:"/process",
    //   the second weight is from weight variable defined earlier
      type: "POST", 
      data:{weight: weight,
      height: height,
      unit: aUnit},
    //   dataType: 'json',   //you may use jsonp for cross origin request
    //   crossDomain: true,
      error: function() {
        alert("Error");
      },
      success: function(data, status, xhr) {
        var bmi = data.bmi
        // debugger  
        if (bmi < 18.5) {
            document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value is Under Weight"+"<br>";
        } else if ((bmi >= 25) && (bmi <= 29.9)) {
            document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value is Over Weight"+"<br>";
        } else if (bmi >= 30) {
            document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value is Obesse"+"<br>";
        } else {
            document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value normal"+"<br>";
        }
    }})
}

function clear(){
    debugger
    document.querySelector(".output_space > p").innerHTML = "The Output Area";

    /* Restore Original Color and Opacity */
    this.setAttribute("usrOn", "0")
    let origO=this.getAttribute("origO")
    let origC=this.getAttribute("origC")

    /* These won't work for non-user defined attributes 
    this.setAttribute("opacity", origO);
    this.setAttribute("backgroundColor", origC);
    */
   this.style.backgroundColor=origC;
   this.style.opacity=origO;

   let inWeight = document.querySelector(".weight_input");
   /* inWeight.style.placeholder="kg" */
   inWeight.value=""
   /*document.querySelector(".weight").style.opacity=1;
   document.querySelector(".weight").style.backgroundColor="#FFFFFF";*/
   let inHeight = document.querySelector(".height_input"); 
   /* inHeight.style.placeholder="cm or m" */
   inHeight.value=""
   /*document.querySelector(".height").style.opacity=1;
   document.querySelector(".height").style.backgroundColor=rgb(255,255,255);*/
   let mButton=document.getElementById('m')
   let cmButton=document.getElementById('cm')
   if (mButton.checked == false) {
        cmButton.checked = false;
        mButton.checked = true;
   }
}


// addEventListener is a method to listen to an event (click, mouse, keypress),
// and handle the event

// != refers to NOT
if(document.getElementById("bmi") != null){
    document.querySelector("#bmi").addEventListener("click", bmi);
}
if(document.getElementById("clear") != null){
    document.querySelector("#clear").addEventListener("click", clear);
}
