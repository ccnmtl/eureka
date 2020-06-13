it('Tests the ear training index template', function() {
    cy.visit('/ear-training/');
    cy.injectAxe();
    cy.checkA11y();
});

