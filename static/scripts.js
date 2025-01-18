document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('searchButton').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent page reload on form submission
    
    const query = document.getElementById('searchQuery').value.trim();
    console.log("Search button clicked");

    // Ensure the query is not empty
    if (query === '') {
        alert("Please enter a search term.");
        return;
    }

    url = `https://test-repo-aqpv.onrender.com/search?q=${query}`;
    try {
        console.log("make response");
        const response = fetch(url);
        if (!response.ok) {
          throw new Error(`Response status: ${response.status}`);
        }
        const json = response.json();
        console.log(json);
      } catch (error) {
        console.log(error);
      }
    });
});
