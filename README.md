# MEMORIA DIGITAL MUJERES VÍCTIMAS DE VIOLENCIA DE GÉNERO — España 2003–2026

Prototipo de memorial digital.

- Arquitectura histórica preparada para 2003–2026.
- Primera capa nominal: 2024.
- El año 2024 se muestra explícitamente en el muro y en cada ficha.
- Orden cronológico corregido usando fechas ISO (`YYYY-MM-DD`).
- Los años todavía no incorporados permanecen como estructura futura y no se rellenan con datos inventados.

**Fuente oficial:** Delegación del Gobierno contra la Violencia de Género, Ministerio de Igualdad.
**Fuente nominal del prototipo 2024:** EFE, recopilación publicada el 31/12/2024.

La cifra oficial y la identificación nominal se mantienen diferenciadas.



# Memoria Digital

## A digital memorial for women victims of gender-based violence in Spain

**Memoria Digital** is an open-source digital memorial created to give individual visibility and remembrance to women who have been murdered by gender-based violence in Spain.

The project transforms publicly available information into a non-anonymous digital memory: instead of presenting only aggregated statistics, it gives visibility to the individual names behind the numbers.

The memorial is designed as a public digital space that can be shared, referenced and preserved as an act of remembrance.

---

## Why Memoria Digital?

Official statistics are essential for understanding the scale of gender-based violence. However, aggregated numbers can make individual lives disappear behind a statistic.

Memoria Digital explores another approach:

> **From statistics to names. From data to memory.**

The project uses publicly available information to construct a structured digital memorial while maintaining a clear distinction between AI-assisted processing and verification.

---

## AI-assisted methodology

A key component of the project is the use of **AI to assist in structuring publicly available information at scale**.

AI can help transform information from public sources into a structured format that can subsequently be processed by the system.

However, AI-generated information is **not allowed to enter the memorial automatically**.

The project therefore introduces a separate deterministic validation layer.

### Pipeline

```text
Public information
        ↓
       AI
        ↓
Structured JSON
        ↓
      Schema
        ↓
Deterministic Validator
        ↓
   ACCEPT / REJECT
        ↓
  Memoria Digital

```

This separation is intentional.

**AI assists with data structuring. Deterministic rules control what can be accepted.**

---

## Deterministic validation

The validation layer checks AI-generated structured records before they can be considered for incorporation into the memorial.

The validator checks:

* required fields
* allowed fields
* year and year range
* name
* date format
* source
* source document
* verification status
* unexpected or invalid data types

A record that does not comply with the predefined rules is rejected.

In particular:

```text
verified = true
        ↓
      ACCEPT

verified = false
        ↓
      REJECT
```

The validator does not generate information or modify the record. It only applies predefined rules and returns an explicit **ACCEPT** or **REJECT** decision.

---

## Automated testing

The validation layer is accompanied by automated tests covering both valid and invalid records.

The tests verify that the system can reject, among other cases:

* missing required information
* invalid dates
* unexpected fields
* unverified records

GitHub Actions automatically runs these tests when relevant files are modified.

This provides a reproducible technical check of the validation layer rather than relying only on manual inspection.

---

## Technical architecture

The AI pipeline is organized as follows:

```text
ai_pipeline/
│
├── schemas/
│   └── memorial_schema.json
│
├── validation/
│   └── validator.py
│
├── tests/
│   └── test_validator.py
│
└── README.md
```

The continuous integration workflow is located at:

```text
.github/
└── workflows/
    └── validate.yml
```

### Main components

**`memorial_schema.json`**

Defines the expected structure of a memorial record and prevents unspecified fields from being accepted.

**`validator.py`**

Implements deterministic validation rules and produces an ACCEPT or REJECT result.

**`test_validator.py`**

Tests the validator using valid and deliberately invalid examples.

**`validate.yml`**

Runs the validation tests automatically through GitHub Actions.

---

## Data and sources

Memoria Digital is based on publicly available information and official sources.

The project aims to preserve a clear distinction between:

1. information obtained from public sources;
2. AI-assisted structuring of that information;
3. deterministic validation;
4. presentation in the digital memorial.

The validation layer does **not** claim that a source is factually true simply because a record passes the validator. Its purpose is to ensure that records comply with predefined structural and verification requirements.

---

## Open source

Memoria Digital is developed as an open-source project.

The source code makes the methodology visible and allows the technical approach to be inspected rather than presenting AI processing as a black box.

The repository contains both the digital memorial and the experimental AI-assisted data pipeline.

---

## Project concept

Memoria Digital explores how AI can be used not simply to generate content, but to help transform large amounts of publicly available information into a structured and human-centred form of digital remembrance.

The central principle is:

> **Technology should help preserve memory, not replace the responsibility of verification.**

---

## Current scope

The current AI pipeline is intentionally maintained as an independent validation component.

It demonstrates the architecture and technical approach without automatically modifying the live memorial data.

This separation allows the existing memorial to remain stable while the AI-assisted processing and validation methodology can be developed and tested independently.

---

## Future development

Possible future developments include:

* processing larger collections of public information;
* expanding the number of structured records;
* improving source traceability;
* integrating additional validation rules;
* connecting validated records to the memorial through a controlled ingestion process.

These developments would maintain the same principle:

```text
AI-assisted processing
        +
Deterministic validation
        =
Controlled digital memory
```

---

## Repository

The project source code, validation architecture and automated tests are available in this repository.

**Memoria Digital** is an ongoing exploration of how artificial intelligence, open data and digital technology can contribute to preserving individual memory and making historical data more human.

