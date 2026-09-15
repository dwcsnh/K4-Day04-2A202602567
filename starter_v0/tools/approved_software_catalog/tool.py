from __future__ import annotations

from typing import Any
import re
from tools._shared import err

SOFTWARE_DB = {
    "visual studio code": {
        "status": "approved",
        "version": "1.80+",
        "notes": "Approved for all developers. Extensions must be reviewed by security before installation."
    },
    "docker": {
        "status": "approved",
        "version": "latest",
        "notes": "Docker Desktop is approved. Requires WSL2 on Windows."
    },
    "wireshark": {
        "status": "restricted",
        "version": "4.0+",
        "notes": "Only approved for Network Engineers. Unauthorized use will trigger an alert."
    },
    "utorrent": {
        "status": "denied",
        "version": "none",
        "notes": "P2P file sharing software is strictly prohibited on company networks."
    },
    "chatgpt": {
        "status": "restricted",
        "version": "web",
        "notes": "Use is permitted for general inquiries, but strictly NO pasting of source code or confidential data."
    },
    "notion": {
        "status": "denied",
        "version": "none",
        "notes": "Not approved for storing company data due to data residency policies. Use internal Confluence instead."
    }
}

def approved_software_catalog(software_name: str) -> dict[str, Any]:
    """
    Look up if a software is approved for use within the company and get installation notes or restrictions.
    """
    try:
        if not software_name or not isinstance(software_name, str):
            raise ValueError("software_name must be a non-empty string.")
            
        search_key = software_name.strip().lower()
        
        # Simple substring matching
        matched_software = None
        for key in SOFTWARE_DB.keys():
            if key in search_key or search_key in key:
                matched_software = key
                break
                
        if matched_software:
            return {
                "tool": "approved_software_catalog",
                "software_name": software_name,
                "match_found": True,
                "catalog_info": SOFTWARE_DB[matched_software]
            }
        else:
            return {
                "tool": "approved_software_catalog",
                "software_name": software_name,
                "match_found": False,
                "message": f"Software '{software_name}' not found in the catalog. It must undergo security review before installation."
            }
    except Exception as exc:
        return err("approved_software_catalog", exc)
