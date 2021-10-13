$(document).ready( () => {
  $("#user_form").submit(e => {
    e.preventDefault();
    const fields = {};
    const setField = (k, v) => fields[k] = v;
    // for(let i=0; i<e.target.length; i++){
    //   if(e.target[i].type === "text"){
    //     fields[e.target[i].name] = e.target[i].value;
    //   }
    // }
    // console.log(fields);
    // alert("thank you for submitting the form.");
    // const response = $.post("/users/new", $("#user_form").serialize());
    // const responseStr = $("#user_form").serialize();
    // const response = responseStr.split("&").map(item => item.split("=")).map(item => setField(item[0], item[1]));
    // for(let datum of response){
    //   const separated = datum.split("=");
    //   fields[separated[0]] = separated[1];
    // }
    console.log($("#user_form").serialize());
    $("#user_form").serialize().split("&").map(pair => setField(...pair.split("=")));
    console.log(fields);
    const newRow = (
      `<tr><td>${fields.first_name}</td><td>${fields.last_name}</td></tr>`
    );
    console.log(newRow);
    $("#users_table").append(newRow);
  });


});