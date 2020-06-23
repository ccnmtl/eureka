import { OpenSheetMusicDisplay } from 'opensheetmusicdisplay';

// Render music notation examples
const BOTTOM_MARGIN_ADJUSTMENT = 140;
let mContainers = Array.from(
    document.getElementsByClassName('music-container'));

let osmdOptions = {
    drawingParameters: 'compacttight',
    drawPartNames: false,
};

mContainers.map((el, idx) => {
    el.id = 'music-container-' + idx;
    let osmd = new OpenSheetMusicDisplay(el, osmdOptions);
    osmd.load(el.dataset.musicxml)
        .then(() => {osmd.render();})
        .then(() => {
            // Fix the height of the examples, temp fix until
            // OpenSheetMusicDisplay fixes this issue:
            // https://github.com/opensheetmusicdisplay/opensheetmusicdisplay/issues/788
            let svg = el.getElementsByTagName('svg')[0];
            // Adjust the height
            let height = (
                Number(svg.getAttribute('height')) - BOTTOM_MARGIN_ADJUSTMENT);
            svg.setAttribute('height', height);
            // Adjust the viewBox
            let viewBox = svg.getAttribute('viewBox').split(' ');
            viewBox[3] = String(height);
            svg.setAttribute('viewBox', viewBox.join(' '));
        });
});

