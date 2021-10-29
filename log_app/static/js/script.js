const validateWorkout = w => {
  const errors = {};
  if(!w.type){
    errors.type = "Workout type is required.";
  }
  let validDate = false;
  try{
    const d = new Date(w.date);
    validDate = (d.toString() !== "Invalid Date");
  }catch{
    validDate = false;
  }
  if(!validDate){
    errors.date = "Please enter a valid date (format: YYYY-MM-DD)";
  }
  const duration = parseInt(w.duration);
  if(isNaN(duration) || duration <= 0){
    errors.duration = "Duration must be a number greater than 0."
  }
  return errors;
};

const displayErrorMessages = errors => {
  let isValid = true;
  if(errors.type){
    isValid = false;
    $("#error_type").text(errors.type);
    $("#error_duration").text("&nbsp;");
  } else {
    $("#error_type").text("");
  }
  if(errors.date){
    isValid = false;
    $("#error_date").text(errors.date);
  } else {
    $("#error_date").text(errors.type ? "\u00A0" : "");
  }
  if(errors.duration){
    isValid = false;
    $("#error_duration").text(errors.duration);
  } else {
    $("#error_duration").text("");
  }
  return isValid;
};

const clearFields = (...fields) => {
  console.log(fields);
  for(let field of fields){
    $(field).val("");
  }
};

$(document).ready( () => {
  $("#new_workout").submit(e => {
    e.preventDefault();
    const w = {
      type: $("#type").val(),
      duration: $("#duration").val(),
      date: $("#date").val(),
    };
    const errors = validateWorkout(w);
    for(let error in errors){
      console.log(`${error} error`);
    }
    console.log("*".repeat(20));
    const isValid = displayErrorMessages(errors);
    if(isValid){
      const response = $.post("/workouts/create/return_row", $("#new_workout").serialize());
      response.done(row => {
        console.log(row);
        $("#workouts_table").append(row);
      });
    }
  });
});