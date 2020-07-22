it('Tests the ear training level template', function() {
    cy.visit('/ear-training/ear-training-one/');
    cy.injectAxe();
    cy.checkA11y();
});

