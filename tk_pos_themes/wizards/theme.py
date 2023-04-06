# -*- coding: utf-8 -*-
# Copyright 2020-Today TechKhedut.
# Part of TechKhedut. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class Theme(models.TransientModel):
    _name = "pos.theme.settings"
    _description = "POS Theme Settings"

    def _get_active_theme(self):
        return self.env['pos.theme.type'].sudo().search([], limit=1).name

    name = fields.Selection([
        ('default', "Default"),
        ('back_to_earth', "Back to Earth"),
        ('dark_shine', "Dark Shine"),
        ('fresh_lemon', "Fresh Lemon"),
        ('lime', "Lime"),
        ('blue', "Ocean Blue"),
        ('orange', "Orange Coral"),
        ('roseanna', 'Roseanna'),
        ('sunshine', "Sunshine"),
        ('purple', "80's Purple"),
    ], required=True, default=_get_active_theme, string="Theme Type")

    @api.onchange('name')
    def onchange_name(self):
        theme = self.sudo().env.ref('tk_pos_themes.pos_theme_type')
        if theme:
            theme.name = self.name

    def set_theme(self):
        name = self.env['pos.theme.type'].sudo().search([], limit=1).name
        themes = [
            'tk_pos_themes.tk_pos_theme_lime',
            'tk_pos_themes.tk_pos_theme_roseanna',
            'tk_pos_themes.tk_pos_theme_blue',
            'tk_pos_themes.tk_pos_theme_orange',
            'tk_pos_themes.tk_pos_theme_dark_shine',
            'tk_pos_themes.tk_pos_theme_purple',
            'tk_pos_themes.tk_pos_theme_back_to_earth',
            'tk_pos_themes.tk_pos_theme_fresh_lemon',
            'tk_pos_themes.tk_pos_theme_sunshine',
        ]
        for thm in themes:
            if name in thm:
                self.env.ref(thm).active = True
            else:
                self.env.ref(thm).active = False

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }


class ThemeType(models.Model):
    _name = "pos.theme.type"

    name = fields.Selection([
        ('default', "Default"),
        ('back_to_earth', "Back to Earth"),
        ('dark_shine', "Dark Shine"),
        ('fresh_lemon', "Fresh Lemon"),
        ('lime', "Lime"),
        ('blue', "Ocean Blue"),
        ('orange', "Orange Coral"),
        ('roseanna', 'Roseanna'),
        ('sunshine', "Sunshine"),
        ('purple', "80's Purple"),
    ], required=True, default='default', string="Theme Type")