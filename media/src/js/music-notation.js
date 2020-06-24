import { OpenSheetMusicDisplay } from 'opensheetmusicdisplay';

// Render music notation examples
let mContainers = Array.from(
    document.getElementsByClassName('music-container'));

let osmdOptions = {
    drawingParameters: 'compacttight',
    drawPartNames: false,
    pageFormat: 'endless',
    autoResize: false,
};

const BOTTOM_MARGIN_ADJUSTMENT = 140;
let setOsmdHeight = (svg, height) => {
    // Fix the height of the examples, temp fix until
    // OpenSheetMusicDisplay fixes this issue:
    // https://github.com/opensheetmusicdisplay/opensheetmusicdisplay/issues/788

    // Adjust the height
    svg.setAttribute('height', height);

    // Adjust the viewBox
    let viewBox = svg.getAttribute('viewBox').split(' ');
    viewBox[3] = String(height);
    svg.setAttribute('viewBox', viewBox.join(' '));
};

mContainers.map((el, idx) => {
    el.id = 'music-container-' + idx;
    let osmd = new OpenSheetMusicDisplay(el, osmdOptions);
    osmd.load(el.dataset.musicxml)
        .then(() => {
            osmd.EngravingRules.PageBottomMargin = 0.0;
            osmd.render();
        })
        .then(() => {
            let svg = el.getElementsByTagName('svg')[0];
            let height = (
                Number(svg.getAttribute('height')) - BOTTOM_MARGIN_ADJUSTMENT);
            setOsmdHeight(svg, height);
        });
});

