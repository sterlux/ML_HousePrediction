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
        <div class="input-field col s3" style="margin-top: 30px;">
          <select id="${column.title.toLowerCase()}" name="${column.title.toLowerCase()}">
            ${column.options
              .map(
                (option) =>
                  `<option value="${option.value}">${option.text}</option>`
              )
              .join("")}
          </select>
          <label>${column.title}</label>
          <span class="helper-text truncate tooltipped" data-position="bottom" data-tooltip="${
            column.helper
          }">${column.helper}</span>
        </div>
      `;
    } else {
      // Render input fields
      const includeYear =
        column.title.toLowerCase().includes("year") ||
        column.title.toLowerCase().includes("yr");
      html += `
        <div class="input-field col s3" style="margin-top: 30px;">
          <input id="${column.title.toLowerCase()}" name="${column.title.toLowerCase()}" type="number" class="validate" value="${
        includeYear ? 2010 : 0
      }" />
          <label for="${column.title.toLowerCase()}">${column.title}</label>
          <span class="helper-text truncate tooltipped" data-position="bottom" data-tooltip="${
            column.helper
          }">${column.helper}</span>
        </div>
      `;
    }
  }
  html += "</div>";

  appDiv.innerHTML = html;

  const elems = document.querySelectorAll("select");
  M.FormSelect.init(elems);
  M.updateTextFields();
  var tooltips = document.querySelectorAll(".tooltipped");
  var instances = M.Tooltip.init(tooltips);
}
