/* eslint-disable max-len */
it('Tests the home page', function() {
    cy.visit('/');
    cy.injectAxe();
    cy.checkA11y();
});

