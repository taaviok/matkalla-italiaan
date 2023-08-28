var lmap;
var marker1 = L.marker([0.0, 0.0]);
var marker2 = L.marker([0.0, 0.0]);

function map_init_basic(map, options) {
  lmap = map;
}

function markCity() {
  var city1 = document.getElementById('icity1').value;
  var city2 = document.getElementById('icity2').value;

  const city1URL = 'https://nominatim.openstreetmap.org/search?q=' + city1 + '&format=geojson';

  fetch(city1URL)
    .then(response => response.json())
    .then(data => {
      
      let coordinates = data.features[0].geometry.coordinates;
      coordiantes = coordinates.reverse();
      marker1.removeFrom(lmap)
      marker1 = L.marker(coordinates);
      marker1.addTo(lmap);
    })

  const city2URL = 'https://nominatim.openstreetmap.org/search?q=' + city2 + '&format=geojson';

  fetch(city2URL)
    .then(response => response.json())
    .then(data => {

      let coordinates = data.features[0].geometry.coordinates;
      coordiantes1 = coordinates.reverse();
      marker2.removeFrom(lmap)
      marker2 = L.marker(coordinates);
      marker2.addTo(lmap);
    })
}

