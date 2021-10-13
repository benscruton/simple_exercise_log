$(document).ready( () => {
  $("#user_form").submit(e => {
    e.preventDefault();
    const fields = {};
    const setField = (k, v) => fields[k] = v;
    $("#user_form").serialize().split("&").map(pair => setField(...pair.split("=")));
    const newRow = (
      `<tr><td>${fields.first_name}</td><td>${fields.last_name}</td></tr>`
    );
    $("#users_table").append(newRow);

    for(let i=1; i<=2; i++){
      $("#user_form")[0][i].value = "";
    }
  });


});