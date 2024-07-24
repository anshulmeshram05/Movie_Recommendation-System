document.getElementById('recommendation-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const movieName = document.getElementById('movie').value;

    fetch(`/recommend?movie=${movieName}`)
        .then(response => response.json())
        .then(data => {
            const recommendationsDiv = document.getElementById('recommendations');
            recommendationsDiv.innerHTML = '';

            data.recommendations.forEach(title => {
                const movieItem = document.createElement('div');
                movieItem.className = 'movie-item';
                movieItem.textContent = title;

                movieItem.addEventListener('click', () => {
                    fetch(`/details?title=${title}`)
                        .then(response => response.json())
                        .then(details => {
                            const detailsDiv = document.createElement('div');
                            detailsDiv.className = 'movie-details';
                            detailsDiv.innerHTML = `
                                <h2>${details.title}</h2>
                                <p>${details.description}</p>
                                <p><strong>Year:</strong> ${details.year}</p>
                                <p><strong>Cast:</strong> ${details.cast}</p>
                                <p><strong>Director:</strong> ${details.director}</p>
                                <p><strong>Genres:</strong> ${details.genres}</p>
                                <p><strong>Runtime:</strong> ${details.runtime} minutes</p>
                                <p><strong>Vote Average:</strong> ${details.vote_average}</p>
                            `;

                            recommendationsDiv.innerHTML = '';
                            recommendationsDiv.appendChild(detailsDiv);
                        });
                });

                recommendationsDiv.appendChild(movieItem);
            });
        });
});
