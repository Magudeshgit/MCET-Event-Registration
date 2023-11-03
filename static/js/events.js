const prevBtns = document.querySelectorAll(".btn-prev");
const nextBtns = document.querySelectorAll(".btn-next");
const progress = document.getElementById("progress");
const formSteps = document.querySelectorAll(".step-forms");
const progressSteps = document.querySelectorAll(".progress-step");

const form = document.querySelector(".form");
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0]
const url = 'http://127.0.0.1:8000/eventsreg/'

let formStepsNum = 0;

nextBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    formStepsNum++;
    submitprocess();
    updateFormSteps();
    updateProgressbar();
    
   
  });
});

prevBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    formStepsNum--;
    updateFormSteps();
    updateProgressbar();
    
  });
});


function submitprocess(e){
  e.preventDefault()
  console.log("Sdf")
    const pname = document.querySelector(".papername").value
    const teamsize = document.querySelector(".teamsize").value
    const member1 = document.querySelector(".member1").value
    const roll1 = document.querySelector(".roll1").value
    const member2 = document.querySelector(".member2").value
    const roll2 = document.querySelector(".roll2").value
  console.log(csrf)
    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf)
    fd.append('pname', pname)
    fd.append('teamsize', teamsize)
    fd.append('member1', member1)
    fd.append('roll1', roll1)
    fd.append('member2', member2)
    fd.append('roll2', roll2)

    $.ajax({
      type: 'POST',
      url: url,
      enctype: "multipart/form-data",
      data: fd,
      success: function(response){
        console.log(response)
      }

    })
}
function updateFormSteps() {
  formSteps.forEach((formStep) => {
    formStep.classList.contains("step-forms-active") &&
      formStep.classList.remove("step-forms-active");
  });

  formSteps[formStepsNum].classList.add("step-forms-active");
}

function updateProgressbar() {
  progressSteps.forEach((progressStep, idx) => {
    if (idx < formStepsNum + 1) {
      progressStep.classList.add("progress-step-active");
      
    } else {
      progressStep.classList.remove("progress-step-active");
   
    }
  });

  progressSteps.forEach((progressStep, idx) => {
    if (idx < formStepsNum) {
      
      progressStep.classList.add("progress-step-check");
    } else {
   
      progressStep.classList.remove("progress-step-check");
    }
  });
 
  const progressActive = document.querySelectorAll(".progress-step-active");

  progress.style.width =
    ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";
}


// document.getElementById("submit-form").addEventListener("click", function () {

//     progressSteps.forEach((progressStep, idx) => {
//     if (idx <= formStepsNum) {
      
//       progressStep.classList.add("progress-step-check");
//     } else {
   
//       progressStep.classList.remove("progress-step-check");
//     }
//   });
  
//    var forms = document.getElementById("forms");
//    forms.classList.remove("form");
//    forms.innerHTML = '<div class="welcome"><div class="content"><svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52"><circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none"/><path class="checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8"/></svg><h2>Thanks for signup!</h2><span>We will contact you soon!</span><div></div>';
// });