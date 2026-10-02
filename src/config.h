#ifndef CONFIG_H
#define CONFIG_H

/*
 * SPDX-License-Identifier: Apache-2.0
 * Copyright (C) 2020-2025 Raspberry Pi Ltd
 * Copyright (C) 2026 Katmera / Atrium
 */


/* Repository URL — future hosted Katmera Repository JSON V4 catalog.
 * Until downloads.katmera.com is live, run with:
 *   katmera-imager --repo /path/to/katmera/catalog/os_list_v4.json
 */
#define OSLIST_URL                              "https://downloads.katmera.com/imager/os_list_v4.json"

/* Custom repository manifest file extension (without leading dot) */
#define MANIFEST_EXTENSION                      "katmera-imager-manifest"

/* MIME type for manifest files */
#define MANIFEST_MIME_TYPE                      "application/vnd.katmera.imager-manifest+json"

/* Time synchronization URL (only used on linuxfb QPA platform, URL must be HTTP) */
#define TIME_URL                                "http://downloads.katmera.com/"

/* Telemetry disabled for Katmera builds (empty URL is a no-op) */
#define TELEMETRY_URL                           ""

/* Hash algorithm for verifying (uncompressed image) checksum */
#define OSLIST_HASH_ALGORITHM                   QCryptographicHash::Sha256

/* Update progressbar every 0.1 second */
#define PROGRESS_UPDATE_INTERVAL                100

/* Default block size for buffer allocation (dynamically adjusted at runtime) */
#define IMAGEWRITER_BLOCKSIZE                   1*1024*1024

/* Enable caching */
#define IMAGEWRITER_ENABLE_CACHE_DEFAULT        true

/* Do not cache if it would bring free disk space under 5 GB */
#define IMAGEWRITER_MINIMAL_SPACE_FOR_CACHING   5*1024*1024*1024ll

#endif // CONFIG_H
