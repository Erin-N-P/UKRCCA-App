function pageSwitch(event){
    event.preventDefault();
    window.location.replace("{% url 'home' %}");
}

