var converter=document.getElementById("convert"),
    page_body=document.getElementsByTagName("body")[0],
    title    = document.getElementsByTagName("h2")[0],
    jumbo    =document.getElementsByClassName("jumbotron")[0];
converter.onclick=()=>{
    page_body.classList.toggle("mode")
    title.classList.toggle("mode")
    jumbo.classList.toggle("bg-dark")
    converter.classList.toggle("btn-light")
}
var type=new Typed("#title",
{
	strings:["hello","Let's Do Something ... Together You can Mangment You Time And Your Tasks  "],
	typeSpeed:50
	}
)
