// base.js
db = db.getSiblingDB("waze"); // Selecciona la base de datos
db.createCollection("eventos"); // Crea la colección

// Opcional: Insertar datos iniciales
db.eventos.insertOne({
  ejemplo: "Documento de prueba",
  fecha: new Date(),
});
