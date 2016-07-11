/*
 * Copyright (C) 2013  Cable Television Laboratories, Inc.
 *
 * Author: Neha Shanbhag <N.Shanbhag@cablelabs.com>
 * Contact: http://www.cablelabs.com/
 *
 * This file is part of Rygel.
 *
 * Rygel is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * Rygel is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 */

using Gee;

public abstract class UIListing
{
    protected static const string DESCRIPTION = "description";
    protected static const string FORK = "fork";
    protected static const string ICON = "icon";
    protected static const string ICONLIST = "iconList";
    protected static const string LIFETIME = "lifetime";
    protected static const string NAME = "name";
    protected static const string PROTOCOL = "protocol";
    protected static const string PROTOCOL_INFO = "protocolInfo";
    protected static const string SHORT_NAME = "shortName";
    protected static const string UI = "ui";
    protected static const string URI = "uri";
    protected static const string UIID = "uiID";

    public abstract bool match (ArrayList<ProtocolElem>? protocols,
                                ArrayList<FilterEntry> filters);
    public abstract string to_ui_listing (ArrayList<FilterEntry> filters);

    public string to_xml (Gee.HashMap<string, string> hash_map) {
        var sb = new StringBuilder ();
        foreach (var e in hash_map.entries) {
            sb.append_printf ("<%s>%s</%s>\n", e.key, e.value, e.key);
        }

        return sb.str;
    }

    // Convenience method to avoid a lot of inline loops
    public bool filters_match (ArrayList<FilterEntry>? filters,
                               string? name,
                               string? value) {
        if (filters == null || name == null || value == null) {
            return false;
        }

        foreach (var entry in filters) {
            if ((entry != null) && (entry.matches (name, value))) {
                return true;
            }
        }

        return false;
    }
}
