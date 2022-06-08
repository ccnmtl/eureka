it('Tests the improvisation combo template', function() {
    cy.visit('/improvisation-combinations/begining-layering/');
    cy.injectAxe();
    cy.checkA11y();
});

