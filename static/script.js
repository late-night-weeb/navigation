function toggleDetails(id) {
    const details = document.getElementById('details-' + id);
    details.style.display = details.style.display === 'block' ? 'none' : 'block';
}

function updateColorPreview(input) {
    const color = input.value;
    document.getElementById('color-preview').style.background = color;
    input.setAttribute("value", color);  // <-- This makes sure the form submits it
}

function showModal(id) {
    document.getElementById(id).style.display = 'flex';
}

function closeModal(id) {
    document.getElementById(id).style.display = 'none';
}

function updateTileColorPreview(select) {
    const preview = document.getElementById("tile-color-preview");
    preview.style.background = select.value;
}

// Auto-set preview on modal open (if needed)
window.addEventListener("load", () => {
    const colorSelect = document.getElementById("tile-color");
    if (colorSelect) {
        updateTileColorPreview(colorSelect);
    }
});


function openEditModal(tile) {
    document.getElementById('edit-id').value = tile.id;
    document.getElementById('edit-name').value = tile.name;
    document.getElementById('edit-website').value = tile.website;
    document.getElementById('edit-port').value = tile.port;
    document.getElementById('edit-username').value = tile.username;
    document.getElementById('edit-password').value = tile.password;
    document.getElementById('edit-email').value = tile.email;
    document.getElementById('edit-image').value = tile.image;

    document.getElementById('edit-http').checked = tile.protocol === "http";
    document.getElementById('edit-https').checked = tile.protocol === "https";

    document.getElementById('edit-category').value = tile.category;
    document.getElementById('edit-color').value = tile.color;
    updateEditColorPreview(document.getElementById('edit-color'));

    // Set form action to point to the edit endpoint
    document.getElementById('editTileForm').action = `/edit_tile/${tile.id}`;

    document.getElementById('editTileModal').style.display = 'flex';
}

function updateEditColorPreview(select) {
    const preview = document.getElementById("edit-color-preview");
    preview.style.background = select.value;
}


function updateTileColorPreview(select) {
    const preview = document.getElementById("tile-color-preview");
    const selectedColor = select.value;
    preview.style.background = selectedColor;

    // Also update options backgrounds (not reliable cross-browser)
    for (const option of select.options) {
        option.style.background = option.getAttribute('data-color');
        option.style.color = getContrastYIQ(option.getAttribute('data-color'));
    }
}

// Helper function to set text color based on bg for readability
function getContrastYIQ(hexcolor) {
    hexcolor = hexcolor.replace('#', '');
    const r = parseInt(hexcolor.substr(0, 2), 16);
    const g = parseInt(hexcolor.substr(2, 2), 16);
    const b = parseInt(hexcolor.substr(4, 2), 16);
    const yiq = ((r * 299) + (g * 587) + (b * 114)) / 1000;
    return (yiq >= 128) ? 'black' : 'white';
}

window.addEventListener("load", () => {
    const colorSelect = document.getElementById("tile-color");
    if (colorSelect) updateTileColorPreview(colorSelect);
});
