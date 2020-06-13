it('Tests the improvisation combo template', function() {
    cy.visit('/improvisation-combinations/beginins-layering/');
    cy.injectAxe();
    cy.checkA11y();
});

