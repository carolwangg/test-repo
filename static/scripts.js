document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('searchButton').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent page reload on form submission

    url = `../search?`;
    fetch(url)
      .then(response => response.json())
      .then(data =>{
          console.log(data);
          console.log(data[0].hello);
        })
      .catch(error => console.error('Error fetching coordinates:',error));
    });
});
