CKEDITOR_UPLOAD_PATH = "uploads/"  # MEDIA_URL /media/uploads/image.jpg

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
    'awesome_ckeditor': {
        'width': '1024px',
        'toolbar': 'full',
        'colorButton_colors': 'b3dfe3,67bfc7,35aab4,028691,016871,015961,' +  # رنگ‌های اصلی (Primary)
                              '99a8b1,677c8b,4d6677,1a3b50,012137,01253d,' +  # رنگ‌های فرعی (Secondary)
                              'b3bec5,81939f,4e6778,1b3c51,000406,000000,' +
                              'f5bfb9,ef948b,e8695d,c82515,9b1d10,85190e,' +
                              'b3bec5,81939f,4e6778,1b3c51,000406,000000,' +
                              'FFFAF8,FEE4DA,FCB298,DF8260,714231,492B20,' +
                              'F3FEFF,C5FDFF,5FF9FF,00B8D4,005E67,003F42,' +
                              'e0f0e8,80c2a2,28946d,0c7051,08563d,064a33,' +
                              'F9FAFB,E5E7EB,9FA6B2,475569,1E293B,0F172A,' +
                              'e3f2fd,90caf9,42a5f5,1e88e5,1565c0,0d47a1',
        'toolbar_Custom': [
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'RemoveFormat'],
            ['TextColor', 'BGColor'],
            ['JustifyRight', 'JustifyCenter', 'JustifyLeft', 'JustifyBlock'],
            ['NumberedList', 'BulletedList'],
            ['Outdent', 'Indent'],
            ['LineHeight'],
            ['Link', 'Unlink'],
            ['Image', 'Table', 'HorizontalRule', 'PageBreak'],
            ['Source', 'Maximize', 'ShowBlocks']
        ],
        'language': 'en',
        'directionality': 'ltr',
        'contentsCss': ['/static/ckeditor/styles.css', 'output.css'],  # استفاده از استایل‌های جدید
        'extraPlugins': ','.join([
            'templates', 'justify', 'lineheight', 'tabletools', 'tableresize',
            'blockquote', 'showblocks', 'colorbutton', 'panel', 'floatpanel', 'richcombo',
            'bidi', 'pastefromgdocs', 'pastetools', 'stylescombo', 'codesnippet',
        ]),
        'line_height': '1.4em;1.6em;1.8em;2em;2.2em;2.5em;3em',

        # فونت‌ها
        'font_names': 'Vazirmatn, sans-serif; ' +
                      'Arial, Helvetica, sans-serif; ' +
                      'Comic Sans MS, cursive; ' +
                      'Courier New, Courier, monospace; ' +
                      'Georgia, serif; ' +
                      'Lucida Sans Unicode, Lucida Grande, sans-serif; ' +
                      'Tahoma, Geneva, sans-serif; ' +
                      'Times New Roman, Times, serif; ' +
                      'Trebuchet MS, Helvetica, sans-serif; ' +
                      'Verdana, Geneva, sans-serif;',

        'font_defaultLabel': 'Vazirmatn, sans-serif',
        'stylesSet': [
            # Custom
            {
                "name": 'TOC Level 1',
                "element": 'div',
                "attributes": {
                    'class': 'ckeditor-toc toc-level-1'
                }
            },
            {
                "name": 'TOC Level 2',
                "element": 'div',
                "attributes": {
                    'class': 'ckeditor-toc toc-level-2'
                }
            },
            {
                "name": 'TOC Level 3',
                "element": 'div',
                "attributes": {
                    'class': 'ckeditor-toc toc-level-3'
                }
            },
            {
                "name": "Info Box",
                "element": "div",
                "attributes": {
                    "class": "info-box"
                },
                "styles": {
                    "background-color": "#e0f3ff",
                    "border-right": "4px solid #2196f3",
                    "padding": "1.5rem 1rem 1rem 1rem",
                    "margin": "2rem 0",
                    "border-radius": "8px",
                    "position": "relative",
                    "direction": "rtl"
                }
            },
            {
                "name": "Warning Box",
                "element": "div",
                "attributes": {
                    "class": "warning-box"
                },
                "styles": {
                    "background-color": "#ffeb3b",
                    "border-right": "4px solid #f44336",
                    "padding": "1.5rem 1rem 1rem 1rem",
                    "margin": "2rem 0",
                    "border-radius": "8px",
                    "position": "relative",
                    "direction": "rtl"
                }
            },
            # Default
            {
                "name": "Italic Title",
                "element": "h2",
                "styles": {
                    "font-style": "italic"
                }
            },
            {
                "name": "Subtitle",
                "element": "h3",
                "styles": {
                    "color": "#aaa",
                    "font-style": "italic"
                }
            },
            {
                "name": "Special Container",
                "element": "div",
                "styles": {
                    "padding": "5px 10px",
                    "background": "#eee",
                    "border": "1px solid #ccc"
                }
            },
            {
                "name": "Marker",
                "element": "span",
                "attributes": {
                    "class": "marker"
                }
            },
            {
                "name": "Big",
                "element": "big"
            },
            {
                "name": "Small",
                "element": "small"
            },
            {
                "name": "Typewriter",
                "element": "tt"
            },
            {
                "name": "Computer Code",
                "element": "code"
            },
            {
                "name": "Keyboard Phrase",
                "element": "kbd"
            },
            {
                "name": "Sample Text",
                "element": "samp"
            },
            {
                "name": "Variable",
                "element": "var"
            },
            {
                "name": "Deleted Text",
                "element": "del"
            },
            {
                "name": "Inserted Text",
                "element": "ins"
            },
            {
                "name": "Cited Work",
                "element": "cite"
            },
            {
                "name": "Inline Quotation",
                "element": "q"
            },
            {
                "name": "Language: RTL",
                "element": "span",
                "attributes": {
                    "dir": "rtl"
                }
            },
            {
                "name": "Language: LTR",
                "element": "span",
                "attributes": {
                    "dir": "ltr"
                }
            },
            {
                "name": "Styled Image (left)",
                "element": "img",
                "attributes": {
                    "class": "left"
                }
            },
            {
                "name": "Styled Image (right)",
                "element": "img",
                "attributes": {
                    "class": "right"
                }
            },
            {
                "name": "Compact Table",
                "element": "table",
                "attributes": {
                    "cellpadding": "5",
                    "cellspacing": "0",
                    "border": "1",
                    "bordercolor": "#ccc"
                },
                "styles": {
                    "border-collapse": "collapse"
                }
            },
            {
                "name": "Borderless Table",
                "element": "table",
                "styles": {
                    "border-style": "hidden",
                    "background-color": "#E6E6FA"
                }
            },
            {
                "name": "Square Bulleted List",
                "element": "ul",
                "styles": {
                    "list-style-type": "square"
                }
            },
            {
                "name": "Clean Image",
                "type": "widget",
                "widget": "image",
                "attributes": {
                    "class": "image-clean"
                }
            },
            {
                "name": "Grayscale Image",
                "type": "widget",
                "widget": "image",
                "attributes": {
                    "class": "image-grayscale"
                }
            },
            # {
            #     "name": "Featured Snippet",
            #     "type": "widget",
            #     "widget": "codeSnippet",
            #     "attributes": {
            #         "class": "code-featured"
            #     }
            # },
            {
                "name": "Featured Formula",
                "type": "widget",
                "widget": "mathjax",
                "attributes": {
                    "class": "math-featured"
                }
            },
            {
                "name": "240p",
                "type": "widget",
                "widget": "embedSemantic",
                "attributes": {
                    "class": "embed-240p"
                },
                "group": "size"
            },
            {
                "name": "360p",
                "type": "widget",
                "widget": "embedSemantic",
                "attributes": {
                    "class": "embed-360p"
                },
                "group": "size"
            },
            {
                "name": "480p",
                "type": "widget",
                "widget": "embedSemantic",
                "attributes": {
                    "class": "embed-480p"
                },
                "group": "size"
            },
            {
                "name": "720p",
                "type": "widget",
                "widget": "embedSemantic",
                "attributes": {
                    "class": "embed-720p"
                },
                "group": "size"
            },
            {
                "name": "1080p",
                "type": "widget",
                "widget": "embedSemantic",
                "attributes": {
                    "class": "embed-1080p"
                },
                "group": "size"
            },
            {
                "name": "240p ",
                "type": "widget",
                "widget": "embed",
                "attributes": {
                    "class": "embed-240p"
                },
                "group": "size"
            },
            {
                "name": "360p ",
                "type": "widget",
                "widget": "embed",
                "attributes": {
                    "class": "embed-360p"
                },
                "group": "size"
            },
            {
                "name": "480p ",
                "type": "widget",
                "widget": "embed",
                "attributes": {
                    "class": "embed-480p"
                },
                "group": "size"
            },
            {
                "name": "720p ",
                "type": "widget",
                "widget": "embed",
                "attributes": {
                    "class": "embed-720p"
                },
                "group": "size"
            },
            {
                "name": "1080p ",
                "type": "widget",
                "widget": "embed",
                "attributes": {
                    "class": "embed-1080p"
                },
                "group": "size"
            }
        ]

    }
}
