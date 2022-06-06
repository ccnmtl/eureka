/* eslint-disable max-len */
it('Tests the ear training element template', function() {
    cy.visit('/ear-training/introduction-to-ear-training-one/tempo/landscaping/');
    cy.injectAxe();
    cy.checkA11y();
});

