import { isMacOs } from "react-device-detect";
import { getCell, getColumnHeader, getRowHeader, newTyne, setCell } from "../testing";

describe("checks insert/delete rows/columns", () => {
  beforeEach(() => {
    newTyne(cy);
  });

  it("checks insert/delete rows/columns", () => {
    setCell(cy, "A1", "=1").should("have.text", "1");
    setCell(cy, "A2", "=12").should("have.text", "12");
    setCell(cy, "B1", "=2").should("have.text", "2");
    setCell(cy, "B2", "=22").should("have.text", "22");
    getColumnHeader(cy, "B").rightclick();
    cy.findByRole("menuitem", { name: "Insert 1 column left" }).click();
    getCell(cy, "B1").should("have.text", "");
    getCell(cy, "B2").should("have.text", "");
    getCell(cy, "C1").should("have.text", "2");
    getCell(cy, "C2").should("have.text", "22");
    getRowHeader(cy, "2").rightclick();
    cy.findByRole("menuitem", { name: "Insert 1 row above" }).click();
    getCell(cy, "A2").should("have.text", "");
    getCell(cy, "B2").should("have.text", "");
    getCell(cy, "C2").should("have.text", "");
    getRowHeader(cy, "2").rightclick();
    cy.findByRole("menuitem", { name: "Insert 1 row below" }).click();
    getCell(cy, "A3").should("have.text", "");
    getCell(cy, "B3").should("have.text", "");
    getCell(cy, "C3").should("have.text", "");
    getCell(cy, "A4").should("have.text", "12");
    getCell(cy, "C4").should("have.text", "22");
    getColumnHeader(cy, "B").rightclick();
    cy.findByRole("menuitem", { name: "Insert 1 column right" }).click();
    getCell(cy, "C1").should("have.text", "");
    getCell(cy, "C2").should("have.text", "");
    getCell(cy, "C3").should("have.text", "");
    getCell(cy, "C4").should("have.text", "");
    getCell(cy, "D1").should("have.text", "2");
    getCell(cy, "D2").should("have.text", "");
    getCell(cy, "D3").should("have.text", "");
    getCell(cy, "D4").should("have.text", "22");
    getColumnHeader(cy, "C").rightclick();
    cy.findByRole("menuitem", { name: "Delete column" }).click();
    getCell(cy, "C1").should("have.text", "2");
    getCell(cy, "C2").should("have.text", "");
    getCell(cy, "C3").should("have.text", "");
    getCell(cy, "C4").should("have.text", "22");
    getRowHeader(cy, "3").rightclick();
    cy.findByRole("menuitem", { name: "Delete row" }).click();
    getCell(cy, "A1").should("have.text", "1");
    getCell(cy, "A2").should("have.text", "");
    getCell(cy, "A3").should("have.text", "12");
    getCell(cy, "B1").should("have.text", "");
    getCell(cy, "B2").should("have.text", "");
    getCell(cy, "B3").should("have.text", "");
    getCell(cy, "C1").should("have.text", "2");
    getCell(cy, "C2").should("have.text", "");
    getCell(cy, "C3").should("have.text", "22");
    getCell(cy, "A1").click().type("{shift}{rightArrow}{rightArrow}{downArrow}");
    getCell(cy, "A2").rightclick();
    cy.findByRole("menuitem", { name: "Delete rows 1-2" }).click();
    getCell(cy, "A1").should("have.text", "12");
    getCell(cy, "C1").should("have.text", "22");
    getCell(cy, "A1").click().type("{shift}{rightArrow}{rightArrow}");
    getCell(cy, "B1").rightclick();
    cy.findByRole("menuitem", { name: "Delete columns A-C" }).click();
    getCell(cy, "A1").should("have.text", "");
    getCell(cy, "C1").should("have.text", "");
    setCell(cy, "A1", "A1");
    setCell(cy, "B1", "B1");
    setCell(cy, "A2", "A2");
    setCell(cy, "B2", "B2");
    setCell(cy, "C1", "C1");
    setCell(cy, "C2", "C2");
    getCell(cy, "B2").click().type("{shift}{rightArrow}{rightArrow}");
    getCell(cy, "C2").rightclick();
    cy.findByRole("menuitem", { name: "Insert 3 columns left" }).click();
    getCell(cy, "C1").should("have.text", "");
    getCell(cy, "C2").should("have.text", "");
    getCell(cy, "B2").click().type("{shift}{downArrow}");
    getCell(cy, "B2").rightclick();
    cy.findByRole("menuitem", { name: "Insert 2 rows above" }).click();
    getCell(cy, "A2").should("have.text", "");
    getCell(cy, "A3").should("have.text", "");

    const meta = isMacOs ? "meta" : "ctrl";

    getRowHeader(cy, "3").click().type(`{shift+${meta}+downArrow}`).rightclick();

    cy.findByRole("menuitem", { name: "Delete rows 3-1001", timeout: 1000 }).click();
    getRowHeader(cy, "3").should("not.exist");
  });
});