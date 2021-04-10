var array = ["change-username", "change-password", "change-email", "change-profile-pic"];

function swapHide(className){
    showClass(className);
    for (var i = 0; i < array.length; i++)
    {
        if (array[i] != className)
        {
            hideClass(array[i]);
        }
    }

}

function showClass(className)
{
    var formItems = [...document.getElementsByClassName(className)];
    for (var i = 0; i < formItems.length; i++)
    {
        formItems[i].style.display = "block";
    }
}

function hideClass(className){
    var allItems = [...document.getElementsByClassName(className)];
    for (var i = 0; i < allItems.length; i++)
    {
        allItems[i].style.display = "none";
    }
}
