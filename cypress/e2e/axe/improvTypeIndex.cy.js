it('Tests the improv type index template', function() {
    cy.visit('/improvisation-types/');
    cy.injectAxe();
    cy.checkA11y();
});

