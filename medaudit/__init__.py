"""MedAudit v0.2.0: attribute probes and leakage screens for supplied features.

``medaudit audit`` reads a JSON config, manifest CSV, and row-aligned feature
matrix, then writes a plain-text report. Calibration and prevalence utilities
are metric primitives; they are not automated audit modules in this release.
"""
from . import metrics  # noqa: F401
from . import splits  # noqa: F401
from . import manifest  # noqa: F401
from . import audits  # noqa: F401
from . import audit  # noqa: F401

__version__ = "0.2.0"
__all__ = ["metrics", "splits", "manifest", "audits", "audit", "__version__"]
