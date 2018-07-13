$(document).ready(function(){
  $("#date").datetimepicker({minDate: "+0M", maxDate: "+1M", timeFormat: 'H:mm', minTime:'8:00 am', maxTime:'7:00 pm', stepMinute:30, 'pickerTimeFormat':"h:mm TT"});
});
