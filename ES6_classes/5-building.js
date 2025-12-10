export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number');
    }

    // Vérification si une sous-classe n’a pas redéfini evacuationWarningMessage
    if (
      this.constructor !== Building &&               // pas la classe elle-même
      this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage
    ) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }

    this._sqft = sqft;
  }

  // Getter
  get sqft() {
    return this._sqft;
  }

  // Méthode abstraite
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
