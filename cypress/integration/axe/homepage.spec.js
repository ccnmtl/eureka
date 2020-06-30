/* eslint-disable max-len */
it('Tests the home page', function() {
    cy.visit('/');
    cy.injectAxe();
    cy.get('.dropdown').first().click();
    cy.checkA11y();
});

