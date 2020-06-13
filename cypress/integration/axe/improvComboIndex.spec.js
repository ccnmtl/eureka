it('Tests the improvisation combo index template', function() {
    cy.visit('/improvisation-combinations/');
    cy.injectAxe();
    cy.checkA11y();
});

