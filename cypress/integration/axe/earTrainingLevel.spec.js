it('Tests the ear training level template', function() {
    cy.visit('/ear-training/introduction-to-ear-training-one/');
    cy.injectAxe();
    cy.checkA11y();
});

