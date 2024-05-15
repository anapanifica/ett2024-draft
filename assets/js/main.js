---
---

{% include js/conference.js %}

window.conference.awaitReady().then(() => {
    const map = window.conference.map.getMap();

    if (typeof map !== 'undefined') {
        let main_station = L.marker([59.36248, 18.06152], {
            icon: L.divIcon({
                className: '',
                html: '<span class="fas fa-train"></span> Main Station',
                iconSize: [120, 56]
            })
        }).addTo(map);
    }
});