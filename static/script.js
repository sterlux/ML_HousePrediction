// Fetch the JSON data from the static file
fetch("../static/columns.json")
  .then((response) => response.json())
  .then((data) => {
    renderJSONToHTML(data);
  })
  .catch((error) => {
    console.error("Error fetching the JSON data:", error);
  });

// Function to render the JSON data to HTML
function renderJSONToHTML(data) {
  const appDiv = document.getElementById("variables");

  let html = '<div class="row">';
  for (let column of data) {
    if (column.options) {
      // Render select fields
      html += `
        <div class="input-field col s3">
          <select id="${column.title.toLowerCase()}" name="${column.title.toLowerCase()}">
            ${column.options
              .map(
                (option) =>
                  `<option value="${option.value}">${option.text}</option>`
              )
              .join("")}
          </select>
          <label>${column.title}</label>
          <span class="helper-text">${column.helper}</span>
        </div>
      `;
    } else {
      // Render input fields
      html += `
        <div class="input-field col s3">
          <input id="${column.title.toLowerCase()}" name="${column.title.toLowerCase()}" type="text" class="validate" value="1" />
          <label for="${column.title.toLowerCase()}">${column.title}</label>
          <span class="helper-text">${column.helper}</span>
        </div>
      `;
    }
  }
  html += "</div>";

  appDiv.innerHTML = html;

  const elems = document.querySelectorAll("select");
  const instances = M.FormSelect.init(elems);
}
