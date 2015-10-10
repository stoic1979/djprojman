function validateAddProject() {
    var title = $("#title").val();
    if(title == "")	{
        alert('Enter Project Title');
        return false;
    } 	

    var description = $("#description").val();
    if(description == "")	{
        alert('Enter Project Description');
        return false;
    } 	

    return true;				
}	
				
