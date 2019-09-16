function show(id)
{
    document.getElementById(id).style.display="block";
}
function ask_confirm(link)
{
    if (confirm("Are you sure?")){
        window.location.href = link;
    } 
}