function log(change){

     console("change type",change.type);
     console("change kimmat",change.name);
     console("change kimmat hazirkisi?",change.object[change.name]);


}
function console(){


for(var i=0; i<arguments.length; i++){

	console.log(arguments[i]);
}
}
var obj=Object.create(Object.prototype)
Object.observe(obj,function(m){


	m.forEach(log);
})