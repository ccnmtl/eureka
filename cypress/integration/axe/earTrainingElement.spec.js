/* eslint-disable max-len */
it('Tests the ear training element template', function() {
    cy.visit('/ear-training/ear-training-one/tempo/tempo-with-landscaping/');
    cy.injectAxe();
    cy.checkA11y();
});

