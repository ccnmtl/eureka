it('Tests the improv type template', function() {
    cy.visit('/improvisation-types/landscaping/');
    cy.injectAxe();
    cy.checkA11y();
});

